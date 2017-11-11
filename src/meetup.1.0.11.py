import iot_config
import iot_wifi
import iot_mqtt
import iot_io
import utime
import machine


def sub_callback(topic, msg):
    led.value(int(msg))


led_pin = iot_io.D1  # d1
led = machine.Pin(led_pin, machine.Pin.OUT)

iot_wifi.connect_wifi(iot_config.wifi_ssid, iot_config.wifi_password)
iot_wifi.wlan.ifconfig()

client = iot_mqtt.MQTTClient(client_id=iot_config.mqtt_client, server=iot_config.mqtt_server)
client.set_callback(sub_callback)
client.connect()
utime.sleep_ms(2000)

client.subscribe(iot_config.mqtt_base_topic)
utime.sleep_ms(2000)

while True:
    client.check_msg()
    utime.sleep_ms(100)

client.disconnect()