package com.example.demo.services;

import com.example.demo.models.userModel;
//import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface userService{

    boolean agregarUsuario(userModel usuario);

    List<userModel> recuperarUsuarios();

    void actualizarUsuario(userModel usuario);

    boolean eliminarUsuario(int idUsuario);

    userModel buscarUsuario(int idUsuario);

}
