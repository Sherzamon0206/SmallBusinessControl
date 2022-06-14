function invoice_data(){
    description1 = document.getElementById('description1').value;
    description2 = document.getElementById('description2').value;
    unitprice1 = document.getElementById('unit_price1').value;
    unitprice2 = document.getElementById('unit_price2').value;
    quantity1 = document.getElementById('qty1').value;
    quantity2 = document.getElementById('qty2').value;
    from_name = document.getElementById('from_name').value;
    from_address = document.getElementById('from_address').value;
    to_customer = document.getElementById('to_new_customer').value;
    to_address = document.getElementById('to_address').value;
    invoice_number = document.getElementById('invoice_number').value;
    datestart = document.getElementById('dateStart').value;
    dateend  = document.getElementById('dateEnd').value;

    console.log(description1, description2, unitprice1, unitprice2, quantity1, quantity2)
    var url = /invoice/
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            "data": [{'description': description1, 'unit_price':unitprice1, 'quantity': quantity1},{'description': description2, 'unit_price':unitprice2, 'quantity': quantity2}],
            'from_name':from_name,
            'from_address': from_address,
            'to_customer': to_customer,
            'to_address': to_customer,
            'invoice_number': invoice_number,
            'datestart': datestart,
            'dateend': dateend,
        })
    })
        .then((response) => {
            response.json().then((data) => {
            // console.log(data)
                document.getElementById('Savebutton').innerHTML+=`
                <a href="/${data['media']}" download="/${data['media']}"> Download</a>
                `
                document.getElementById('Savebutton2').innerHTML+=`
                <a href="/${data['media']}" download="/${data['media']}"> Download</a>
                `
            })

        })
}
function newLinejs(){
    document.getElementById('lines').innerHTML+=`<tr class="line">
                                <td class="zap has-tooltip tooltip-left">
                                    <!-- ZAP -->
                                    <button tabindex="-1" type="button" class="btnDeleteRow btn-zap">
                                        <i class="material-icons">&#xe5c9;</i>
                                    </button>
                                    <i class="tip">Delete Line</i>
                                </td>
                                <td class="dropdown-toggle select item">
                                    <label class="hidden-large">Item</label>
                                    <select class="noborder selectItem" onfocusin="objSelected=this;" name="item[]"
                                        id="itemSelect1">
                                        <option value="" selected="selected"></option>
                                        <option value="Service">Service</option>
                                        <option value="Hours">Hours</option>
                                        <option value="Days">Days</option>
                                        <option value="Product">Product</option>
                                        <option value="Discount_aynax">Discount</option>
                                    </select>
                                </td>
                                <td>
                                    <label class="hidden-large">Description</label>
                                    <textarea name="description[]" id="description[]" rows="1" maxlength="1000"
                                        class="growTextarea"></textarea>
                                </td>
                                <td class="price">
                                    <label class="hidden-large">Unit Price</label>
                                    <input type="number" name="unit_price[]" id="unit_price[]"
                                        class="text-right linePrice inputNumber" value="" autocomplete="nope"
                                        placeholder="0.00">
                                </td>
                                <td class="qty">
                                    <label class="hidden-large">Quantity</label>
                                    <input type="number" name="qty[]" id="qty[]" class="text-right lineQty inputNumber"
                                        value="" autocomplete="nope" placeholder="0.00">
                                </td>
                                <td class="amount alertLineTotal">
                                    <label class="hidden-large">Amount</label>
                                    <input type="text" tabindex="-1" name="total[]" id="total[]" class="lineTotal"
                                        value="0.00" readonly>
                                </td>
                            </tr>`
    console.log(document.getElementsByClassName('description').value)
}
