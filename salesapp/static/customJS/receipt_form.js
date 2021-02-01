$(document).ready(() => {
    $("#id_amount").on("keyup",() => {
        // Set amount in words according to amount in numbers
        amount = document.querySelector('#id_amount').value;
        $.ajax({
            type: 'get',
            url: configuration['salesapp']['convert_amount_to_words'],
            data: { 'amount': amount },
            dataType: 'json',
            success: (data) => {
                if (data.success) {
                    document.querySelector('#id_amount_in_words').value = data.amount_in_words;
                }
            },
        });

    })

    $("#id_amount").on("keyup",() => {
        // Set balance from amount and price
        amount = document.querySelector('#id_amount').value;
        item_id = document.querySelector('#id_item').value;
        quantity = document.querySelector('#id_quantity').value;
        $.ajax({
            type: 'get',
            url: configuration['salesapp']['get_balance'],
            data: { 'item_id': item_id, 'amount': amount, "quantity":quantity },
            dataType: 'json',
            success: (data) => {
                if (data.success) {
                    document.querySelector('#id_balance').value = data.balance;
                    if(data.balance < 0){
                       document.querySelector('#feedback').innerHTML = "Amount Insufficient";
                       document.querySelector('#id_balance').value = "";
                    } else {
                    document.querySelector('#feedback').innerHTML = "";
                    }
                }
            },
        });

    })

    $("#id_quantity").on("keyup",() => {
        // Set balance from amount and price
        quantity = document.querySelector('#id_quantity').value;
        item_id = document.querySelector('#id_item').value;
        amount = document.querySelector('#id_amount').value;
        $.ajax({
            type: 'get',
            url: configuration['salesapp']['get_number_in_stock'],
            data: { 'item_id': item_id, 'quantity': quantity, "amount":amount },
            dataType: 'json',
            success: (data) => {
                if (data.number_in_stock) {
                    if(data.number_in_stock < 0){
                       console.log("Working....")
                       document.querySelector('#feedback').innerHTML = data.message;
                       document.querySelector('#id_balance').value = "";
                    } else {
                        document.querySelector('#id_balance').value = data.balance;
                        document.querySelector('#feedback').innerHTML = "";
                    }
                }
            },
        });
    });

});