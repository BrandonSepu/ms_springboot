package com.example.demo.services;

import com.example.demo.dao.userDao;
import com.example.demo.dao.userDaoImp;
import com.example.demo.dao.userDaoJpa;
import com.example.demo.models.userModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
@Service

public class userServiceImp implements userService {

    String msg="";

    @Autowired
    userDaoImp dao;

    @Override
    public boolean agregarUsuario(userModel user) {
        if(dao.recuperarUser(user.getId_user())==null) {
            dao.agregarUser(user);
            msg = "usuario agregado";
            System.out.println(msg);
            return true;
        }
        msg = "usuario no agregado";
        System.out.println(msg);
        return false;
    }

    @Override
    public List<userModel> recuperarUsuarios() {
        msg = "usuarios encontrados";
        System.out.println(msg);
        return dao.devolverUsuarios();
    }

    @Override
    public void actualizarUsuario(userModel user) {
        if (dao.recuperarUser(user.getId_user())!=null){
            dao.actualizarUser(user);
        };
        msg = "usuario no encontrado";
        System.out.println(msg);
    }

    @Override
    public boolean eliminarUsuario(int idUser) {
        if(dao.recuperarUser(idUser)!=null) {
            dao.eliminarUser(idUser);
            msg = "usuario eliminado";
            System.out.println(msg);
            return true;
        }
        msg = "usuario no eliminado";
        System.out.println(msg);
        return false;
    }

    @Override
    public userModel buscarUsuario(int idUser) {
        msg = "usuario encontrado";
        System.out.println(msg);
        return dao.recuperarUser(idUser);
    }

}
