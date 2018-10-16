class Database(object):
    """The class to store our data"""
    def __init__(self):
        """The constructor for the Database"""
        self.products = {}
        self.users = {}
        self.attendants = {}
        self.user_emails_index = {}
        self.sales_details_index = {}
        self.products_name_index = {}