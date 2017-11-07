

Vinst = new Vue({

el: '#testapp', 
delimiters:['[[', ']]'], 
data: { /*add the variables-models-data etc here */

	carmake: 'honda', 
	model: 'civic', 
	price: '',
	postfix: '',
	newval:''
   },
methods: {
changeout: function(price){
    if(price >= 1000000){
		this.newval = (price/1000000);
		this.postfix = "Million JMD"; 
		return this.newval;
	}  
	if(price >= 1000){
		this.newval = (price/1000);
		this.postfix = "Thousand JMD"; 
		return this.newval;
	}  
	if(price < 1000){
		this.newval = (price);
		this.postfix = " JMD"; 
		return this.newval;
	}  
	   
    }
	
},

computed: {
 newprice: function(){

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
