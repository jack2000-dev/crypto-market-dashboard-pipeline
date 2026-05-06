import schedule
import time
from main import main
from log import logger

def job():
    logger.info("Pipeline updating...")
    main()
    logger.info("Data updated")

schedule.every().hour.do(job)

while True:
  try:
    schedule.run_pending()
    time.sleep(1)
  except KeyboardInterrupt:
    logger.info("Scheduler stopped")
    break