import pika, os, javaobj


class Bridge:
    def send(self, queue, message, host):
        url = os.environ.get('CLOUDAMQP_URL', host)
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        channel.queue_declare(queue=queue, durable=True)
        channel.basic_publish(exchange='', routing_key=queue, body=message)

        connection.close()

    def receive(self, queue, host):
        url = os.environ.get('CLOUDAMQP_URL', host)
        params = pika.URLParameters(url)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        channel.queue_declare(queue=queue, durable=True)
        self.i=0
        self.mes = []

        def callback(ch, method, properties, body):
            self.i += 1
            self.mes.append(javaobj.loads(body))
            if (self.i == 2):
                channel.stop_consuming()
                connection.close()

        channel.basic_consume(
            queue=queue, on_message_callback=callback, auto_ack=True)

        channel.start_consuming()
        return self.mes
