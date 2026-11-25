from jsonschema import validate

product = {
    "id": 10,
    "name": "Monitor",
    "price": 15000,
    "in_stock": True,
    "manufacturer": {
         "id": 5,
        "name": "Samsung",
        "country": "South Korea",
    },
}

product_schema = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer",
            "exclusiveMinimum": 0,
        },
        "name": {
            "type": "string",
            "minLength": 3,
            "maxLength": 50,
        },
        "price": {
            "type": "integer",
            "minimum": 1,
            "maximum": 1000000,
        },
        "in_stock": {
            "type": "boolean",
        },
        "manufacturer": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "exclusiveMinimum": 0,},
                "name": {
                    "type": "string",
                    "minimum": 2,
                    "maximum": 100,
                },
                "country": {
                  "type": "string",
                  "minimum": 2,
                  "maximum": 50,  
                },
            },
            "required": ["id", "name", "country"],
            "additionalProperties": False,
        }
    },
    "required": ["id", "name", "price", "in_stock", "manufacturer"], 
    "additionalProperties": False,
}

validate(instance=product, schema=product_schema)

print("Validation passed")
