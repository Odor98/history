broker_ip = '223.194.27.85'
topic = 'ai_platform_v_0_1'


def call_delay(type_name) :
    t = type_name
    if t == 'temp' :
        return 10
    if t == 'humidity' :
        return 10
    if t == 'pm10' :
        return 10
    if t == 'pm25' :
        return 10




if __name__ == "__main__" :
    print(call_delay('temp'))
