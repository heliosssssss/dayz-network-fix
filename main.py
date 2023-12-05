import os
from logzero import logger
import multiprocessing
import psutil
import time
import random

g_author = 'helios'
g_ver = 'v2'
g_lastUpdated = '12/5/2023'
g_title = f'DayZ Network Fix [{g_ver}-active]'
g_isDZSA = False

class init:
    os.system(f"title {g_title}")
    logger.info(f'DayZ Network Fix [{g_ver}-active]')
    logger.info(f'Last updated @ [{g_lastUpdated}] / made by [{g_author}]')

    logger.critical(f'begin @ DZSA instance check')

    for proc in psutil.process_iter():
        time.sleep(random.randint(int(0.01), int(0.99)))
        logger.warning(f'--> process: {proc.name()} @ {proc.pid}')
        if "DZSALauncher.exe" in proc.name():
            logger.info('DZSA-Launcher PUID above context message.')
            g_isDZSA = True
    if g_isDZSA == False:
        logger.critical('Cannot locate DZSALauncher.exe relapsing to differnet PUID')
    else:
        logger.critical('DZSA Launcher has been detected')


input()
