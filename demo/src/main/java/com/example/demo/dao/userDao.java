package com.example.demo.dao;

import com.example.demo.models.userModel;
import org.springframework.stereotype.Component;

import java.util.List;
@Component
public interface userDao {
    void agregarUser(userModel user);

    userModel recuperarUser(String email);

    void eliminarUser(String email);

    List<userModel> devolverUsuarios();

    void eliminarUser(int idUser);

    userModel recuperarUser(int idUser);

    void actualizarUser(userModel user);
}
