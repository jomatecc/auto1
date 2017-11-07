

Vinst = new Vue({
el: '#testapp', 
delimiters:['[[', ']]'], 
data: { /*add the variables-models-data etc here */

	carmake: 'honda', 
	model: 'civic', 
	price: '',
	postfix: ''
   },

computed: {
 newprice: function() {

if(this.price >= 1000000){
	this.postfix = "Million JMD"; 
	return (this.price/1000000);
                     }
if(this.price >= 1000){
	this.postfix = "Thousand JMD"; 
	return (this.price/1000);  
		} 
if (this.price <= 1000){
	this.postfix = "JMD"; 
        return this.price;
        }

 
		   }

	    }

    }
)
