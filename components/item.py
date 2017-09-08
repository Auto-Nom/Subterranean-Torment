"""
Item component for Subterranean Torment
"""

class Item:
    def __init__(self, use_function=None, targeting=False, targeting_message=None, radius=0, **kwargs):
        self.use_function = use_function
        self.targeting = targeting
        self.targeting_message = targeting_message
        self.radius = radius
        self.function_kwargs = kwargs


