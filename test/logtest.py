import logging

def console_out(logfile):
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(filename)s : %(levelname)s %(message)s',
        datefmt='%Y_%m_%d %A %H:%M:%S',
        filename=logfile,
        filemode='w'
    )
    console=logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter=logging.Formatter('%(asctime)s %(filename)s : %(levelname)s %(message)s')
    console.setFormatter(formatter)

    logging.getLogger().addHandler(console)
    logging.debug('debug')
    logging.info('info')
    logging.warning('warning')
    logging.error('error')

if __name__ == '__main__':
    a=console_out('log1.log')

