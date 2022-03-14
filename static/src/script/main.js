function signout(){
    axios({
        method: 'post',
        url: '/signout',
    }).then(res=>{
        return res.data;
    }).then(data=>{
        location='/';
    });
}