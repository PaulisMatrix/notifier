from typing import Tuple


def get_html_content(info: dict) -> Tuple[str, str]:
    # Depending on the order_status, there will be a different msg configured
    # Currently, let's just assume that notification is for PLACED status
    """
    given the event payload, generate the html content body and the subject and return
    """
    if info.get("discount_applied"):
        discount = info.get("total_discount", 0)
    else:
        discount = 0

    body = f"""
        <body>
            <h1>Order Placed Successfully</h1>
            <span>Dear {info.get("user_name","")},</span><br>
            <span>Thank you for your order! We're excited to process your request.</span>

            <h2>Order Details</h2>
            <div>
                <span>Order ID: {info.get("order_id","")}</span><br>
                <span>Order Subtotal: {info.get("currency","")} {info.get("order_subtotal",0)}</span><br>
                <span>Shipping Charges: {info.get("currency","")} {info.get("shipping_charges",0)}</span><br>
                <span>Total Discount: {info.get("currency","")} {discount}</span><br>
                <span>Number of Items: {info.get("num_items",0)}</span>
            </div>
            <h3>Delivery Information</h3>
            <div>
                <span>Order Status: {info.get("order_status","")}</span><br>
                <span>Expected Delivery Date: {info.get("expected_date","")}</span><br>
                <span>Delivery Address: {info.get("delivery_address","")}</span>
            </div>
            <h3>Payment and Tracking</h3>
            <div>
                <span>Payment Mode: {info.get("payment_mode","")}</span><br>
                <span>Tracking ID: {info.get("tracking_id","")}</span><br>
                <span>Carrier Name: {info.get("carrier_name","")}</span>
            </div>
            
            <span>We'll keep you updated on the progress of your order. If you have any questions or concerns, please don't hesitate to contact our customer support team.</span>
            <span>Thank you for choosing our service!</span><br>
            <span>Best regards,<br>
            Notifier</span>
        </body>
    """
    subject = (
        f"""Your order {info.get("order_id","")} of {info.get("num_items",0)} items"""
    )
    return body, subject
