import json
import traceback


class DataProcessor:
    def __init__(self, input_file=None, output=None, logger=None):
        self.data = None
        self.input_file = input_file
        self.output = output
        self.__input_json_data = None
        self.logger = logger

    @property
    def input_json_data(self):
        return self.__input_json_data

    @input_json_data.setter
    def input_json_data(self, value):
        self.__input_json_data = value

    def load_input(self) -> bool:
        """
        Load input json data
        :return:
        """
        try:
            self.logger.debug(f"Loading input json data from {self.input_file}")
            with self.input_file.open() as fp:
                self.input_json_data = json.load(fp)
                self.logger.debug(f"Successfully loaded input data from {self.input_file}")
            return True
        except json.JSONDecodeError as err:
            self.logger.error(f"Encountered JSONDecodeError at {traceback.format_exc()}")
        except Exception as err:
            self.logger.error(f"Failed to parse the input json file! {err}")
        return False

    def transform_data(self) -> dict:
        """
        Process and transform the data
        :return:
        processed_data
        """
        # self.logger.debug(self.input_json_data)
        response = {"errors": None, "result": None}
        processed_data = {"customers": [], "orders": []}
        if self.input_json_data:
            for each_data in self.input_json_data:
                try:
                    self.logger.debug(f"Transforming data for customer id {each_data.get('customer').get('id')}")
                    orders = []
                    customer_info = each_data.pop("customer")
                    customer_id = customer_info.get("id")
                    processed_data['customers'].append(customer_info)
                    order = each_data.pop('order')
                    for item, value in order.items():
                        order_info = {
                            "item": item,
                            "quantity": value.get("quantity"),
                            "price": value.get("price"),
                            "revenue": int(value.get("price")) * int(value.get("quantity"))
                        }
                        orders.append(order_info)
                    orders_info = each_data
                    orders_info['orders'] = orders
                    orders_info['customer'] = customer_id
                    processed_data['orders'].append(orders_info)
                except Exception as err:
                    self.logger.error(f"Failed transforming the data {each_data} with error {err}")
                    response['errors'] = str(err)
            response['result'] = processed_data
            self.logger.debug(f"Transforming data complete")
        else:
            error = "No data passed to transform"
            self.logger.error(error)
            response['errors'] = error
        return response

    def save_data(self, data: dict) -> bool:
        """
        Save the transformed data to file
        """
        try:
            with open(self.output, 'w') as fw:
                self.logger.info(f"Writing the transformed data to {self.output}")
                fw.write(json.dumps(data.get("result"), indent=4))
        except Exception as err:
            self.logger.error(f"Failed while saving transformed data to file with error: {err}")
            return False
        return True
