const cargarUsuario = async () =>{
    let res = await axios.get ("http://localhost:8000/usuarios")
};
cargarUsuario();
