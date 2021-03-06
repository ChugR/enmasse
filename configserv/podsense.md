The podsense service is an AMQP service for doing discovery of pods in an OpenShift cluster. To
do pod discovery, the client must attach a receiver on the address `podsense`.

To narrow the set of discovered pods, a filter map may be specified on the link source. This will be
used as a label map when watching the pods using the OpenShift API. Whenever the
set of pods changes the service will send a message with the following format (using AMQP types):

```
    amqp-value(
        list(
            map <string, *>
                "host": string
                "phase": string
                "ready": string ("True", "False" or "Unknown")
                "ports": map <string, map<string, int>>))
```

The `ports` field has a map from `container name` to another map of `port name` to `port number` for each container.
