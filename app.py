from ddtrace import tracer
import time


def main():
    while True:
        with tracer.trace('main', service="jb-hackathon-2021-py") as span:
            hello()

def hello():
    with tracer.trace('hello') as span:
        time.sleep(5)
        print("hello")

if __name__ == '__main__':
    main()