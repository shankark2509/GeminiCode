import argparse, logging
from alert_tool import AlertTool

if __name__ == '__main__':
    logger = logging.getLogger('AlertingTool')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    parser = argparse.ArgumentParser()
    parser.add_argument("--currency","-c", help="Currency \n The currency trading pair, or ALL",required=True)
    parser.add_argument("--type","-t",help="{pricedev,pricechange,voldev,ALL} \n The type of check to run, or ALL",required=True)
    parser.add_argument("--deviation","-d",help="Deviation \n percentage deviation of the change")
    logger.info("Parsing Command Line Arguments")
    args = parser.parse_args()

    if args.type:
        #24h Price Change with Deviation passed
        if args.type == "pricechange" and args.deviation:
            alert = AlertTool(logger, args.currency, float(args.deviation))
            alert.priceChange()
        #24h Price Change with default Deviation
        elif args.type == "pricechange":
            alert = AlertTool(logger,args.currency,1.0)
            alert.priceChange()
        # Price Standard Deviation  with Standard Deviation passed by user
        elif args.type == "pricedev" and args.deviation:
            alert = AlertTool(logger, args.currency, float(args.deviation))
            alert.priceDeviation()
        # Price Standard Deviation  with default Standard Deviation
        elif args.type == "pricedev":
            alert = AlertTool(logger, args.currency, 1.0)
            alert.priceDeviation()
        # Volume Deviation with threshold passed by user
        elif args.type == "voldev" and args.deviation:
            alert = AlertTool(logger, args.currency, float(args.deviation))
            alert.volumeDeviation()
        # Volume Deviation with default threshold
        elif args.type == "voldev" and args.deviation:
            alert = AlertTool(logger, args.currency, 1.0)
            alert.volumeDeviation()
        # Args type All with deviation passed by user
        elif args.type == "ALL" and args.deviation:
            alert = AlertTool(logger, args.currency, float(args.deviation))
            logger.info("Calling pricechange module")
            alert.priceChange()
            logger.info("Calling standard deviation module")
            alert.priceDeviation()
            logger.info("Calling Volume deviation")
            alert.volumeDeviation()
        # Args type All with default deviation
        elif args.type == "ALL":
            alert = AlertTool(logger, args.currency, 1.0)
            logger.info("Calling pricechange module")
            alert.priceChange()
            logger.info("Calling standard deviation module")
            alert.priceDeviation()
            logger.info("Calling Volume deviation")
            alert.volumeDeviation()
        #Incorrect Arg type passed
        else:
            logger.info("Incorrect argtype. Please enter either - pricedev, pricechange, volchange or ALL")