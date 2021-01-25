$(document).ready(() => {

    $("#id_amount").change(() => {
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

    $("#id_amount").change(() => {
        // Set balance from amount and price
        amount = document.querySelector('#id_amount').value;
        item_id = document.querySelector('#id_item').value;
        $.ajax({
            type: 'get',
            url: configuration['salesapp']['get_balance'],
            data: { 'item_id': item_id, 'amount': amount },
            dataType: 'json',
            success: (data) => {
                if (data.success) {
                    document.querySelector('#id_balance').value = data.balance;
                    if(data.balance < 0){
                       document.querySelector('#feedback').innerHTML = "Amount Insufficient";
                    }
                }
            },
        });

    })

});