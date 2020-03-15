## GET /
get recommended products by customer_id.

### Request

#### Header
```
application/json
```

#### Params
```
{
    "customer_id": SOME_CUSTOMER_ID,
}
```

### Resonse
#### Header
```
application/json
```

#### Body
```json
{
    ["Product_id"]
}
```

## GET /db/get
get products from db for recommendation

### Request

#### Header
```
application/json
```

#### Params
```
{
    "customer_id": SOME_CUSTOMER_ID,
}
```

### Resonse
#### Header
```
application/json
```

#### Body
```json
{
    ["Product_id"]
}
```


## PUT /db/buy
add products to db

### request

#### Header
```
application/json
```

#### Body
```
{
    SOME_PRODUCT_ID,
}
```

### Resonse
#### Header
```
application/json
```

#### Body
```json
{
    "message" : "success"
}
```

### DB modal: UA1
