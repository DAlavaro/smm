# app/smm/cron.py
def my_job():
    try:
        with open('cron_test.log', 'a') as f:
            f.write('Hello, world!\n')
    except Exception as e:
        with open('cron_test.log', 'a') as f:
            f.write('Error\n')
