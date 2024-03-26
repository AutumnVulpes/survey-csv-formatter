import unittest
import functions_to_test


# KeyError, missing key
no_sku_key = {123456 :{
    'backer_details' : {
        'first_name' : 'John'
    },
}
}

# {}
empty_skus = {123456 :{
    'backer_details' : {
        'first_name' : 'John'
    },
    'product_skus' : {}
}
}

#KeyError, missing key
incomplete_keys = {123456: {
    'backer_details': {
        'first_name': 'John'
    },
    'product_skus': {
        'SKU 1': 1
    }
}
}

# TypeError, '>' not supported between instances of 'str' and 'int'
sku_as_str = {123456: {
    'backer_details': {
        'first_name': 'John'
    },
    'product_skus': {
        'SKU 1': 'a'
    }
}
}

class test_dict_to_list(unittest.TestCase):

    def test_no_sku_key(self):
        self.assertEqual(
            create_csv_list(no_sku_key), 
            KeyError, 
            "KeyError, missing the 'product_skus' key."
        )

    def test_empty_skus(self):
        self.assertEqual(
            create_csv_list(empty_skus), 
            [], 
            """Should return an empty list since 'product_skus' exists, 
            but there's no keys inside at all, and hence no value greater than 0."""
        )

    def test_incomplete_keys(self):
        self.assertEqual(
            create_csv_list(incomplete_keys), 
            KeyError, 
            "KeyError, as loop breaks when it can't find 'last_name' key."
        )

    def test_sku_as_str(self):
        self.assertEqual(
            create_csv_list(sku_as_str), 
            TypeError, 
            "TypeError, as '>' not supported between instances of 'str' and 'int'."
        )
if __name__ == '__main__':
    unittest.main()