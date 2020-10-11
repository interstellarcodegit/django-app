const axios = require ('axios');
const token = {
	username:'superoot',
	password:'superuser'


}

axios.get('http://localhost:9000/apis/Users/', {
  auth:token
})
  .then(res => res.json())
  .then(json => console.log(json));
