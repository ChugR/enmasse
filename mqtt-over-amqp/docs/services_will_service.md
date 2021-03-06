# Will Service

The Will Service (WS) has an AMQP receiver on the following control address :

* $mqtt.willservice

This receiver is attached with :

* rcv-settle-mode : first (0)
* snd-settle-mode : unsettled (0)

so that it can provide a QoS 1 (AT_LEAST_ONCE) for receiving messages.

It's able to handle following scenarios :

* receiving “will” information for a new connected client (see “Connection”).
* start publishing “will” due to a brute client disconnection (see “Disconnection”). The WS acts as an AMQP sender on “will-topic” in order to publish the “will”. The QoS level specified with sender and receiver settle modes during the attachment depends on the desired QoS specified in the "will" message (see "Publish").
* removing “will” information for a specific client (see “Disconnection”).
* overwriting “will” information for a specific client (it’s something that we don’t have in the MQTT spec).
