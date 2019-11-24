#!/usr/bin/python
# -*-coding:utf-8-*-
import logging

logging.basicConfig(level=logging.DEBUG,filename='./runlog.log',
                    format='%(asctime)s '
                    '%(filename)s '
                    '[line:%(lineno)d] '
                    '%(levelname)s '
                    '%(message)s')

logging.debug("完全OK")
logging.info("还好")
logging.warning('有一点小问题')
logging.error('有大问题')
logging.critical('瘫痪')






































































