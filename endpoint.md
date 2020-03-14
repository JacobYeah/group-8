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
