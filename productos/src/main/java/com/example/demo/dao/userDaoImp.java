package com.example.demo.dao;

import com.example.demo.models.userModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import javax.transaction.Transactional;
import java.util.List;
@Repository
@Transactional
public class userDaoImp implements userDao{
    @Autowired
    userDaoJpa userjpa;

    @Override
    public void agregarUser(userModel user) {
        userjpa.save(user);
    }

    @Override
    public userModel recuperarUser(String email) {
        //return userjpa.findByEmail(email);
        return null;
    }

    @Override
    public void eliminarUser(String email) {
        //userjpa.deleteByEmail(email);
    }

    @Override
    public List<userModel> devolverUsuarios() {
        return userjpa.findAll();
    }

    @Override
    public void eliminarUser(int idUser) {
        userjpa.deleteById(idUser);
    }

    @Override
    public userModel recuperarUser(int idUser) {
        try{
            return userjpa.findById(idUser).orElse(null);
        }catch (Exception e){
            e.getMessage();
            return null;
        }
    }

    @Override
    public void actualizarUser(userModel user) {
        userjpa.save(user);
    }
}
