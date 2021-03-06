import paho.mqtt.client as mqtt
import ssl
import optparse

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(opts.topic, int(opts.qos))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

def on_log(client, userdata, level, string):
    print(string)

parser = optparse.OptionParser(usage="usage: %prog [options]",
                               description="Receive messages from the supplied address.")

parser.add_option("-c", "--connectHost", default="localhost",
                  help="host to connect to (default %default)")

parser.add_option("-p", "--portHost", default="8883",
                  help="port to connect to (default %default)")

parser.add_option("-t", "--topic", default="mytopic",
                  help="topic to subscribe to (default %default)")

parser.add_option("-q", "--qos", default="0",
                  help="quality of service (default %default)")

parser.add_option("-s", "--serverCert", default="server-cert.pem",
                  help="server certificate file path (default %default)")

opts, args = parser.parse_args()

client = mqtt.Client("recv")
client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log

context = ssl.create_default_context()
context.load_verify_locations(cafile=opts.serverCert)

# just useful to activate for decrypting local TLS traffic with Wireshark
#context.set_ciphers("RSA")

client.tls_set_context(context)
client.tls_insecure_set(True)
client.connect(opts.connectHost, opts.portHost, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
