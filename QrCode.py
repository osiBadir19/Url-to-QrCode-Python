class QrCodeGenrator:
    """
    generate a qr code
    """
    # import required modules
    import pyqrcode
    
    def __init__(self, link: str):
    """
    :param link: the url you want to convert to QRCode.
    """
        self.Qrversion = self.pyqrcode.create(link)
     
     #create a qr image out of on link, save it in current directory.   
    def create_qr_image(self):
    """
    convert the url to a qr image.
    """
        self.Qrversion.svg("tradingjournal.svg", scale=8)
    
