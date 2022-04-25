package com.example.demo.controllers;
import com.example.demo.models.userModel;
import com.example.demo.services.userService;
import com.example.demo.services.userServiceImp;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;


@CrossOrigin(origins = "*")
@RestController
public class userController {

    @Autowired
    userService uService;

    @RequestMapping("/welcome")
    public String welcomepage() {
        return "Welcome to Yawin Tutor";
    }

    @GetMapping(value = "/users", produces = MediaType.APPLICATION_JSON_VALUE)
    public List<userModel> getAllUsers() {
        return uService.recuperarUsuarios();
    }

    @GetMapping(value = "/user/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
    public userModel recuperarUser(@PathVariable("id") int id) {
        return uService.buscarUsuario(id);
    }

    @PostMapping(value = "/load", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.TEXT_PLAIN_VALUE)
    public String saveUser(@RequestBody userModel user1) {
        return String.valueOf(uService.agregarUsuario(user1));
    }

    @PutMapping(value = "/update", consumes = MediaType.APPLICATION_JSON_VALUE)
    public void actualizarUser(@RequestBody userModel user) {
        uService.actualizarUsuario(user);
    }

    @DeleteMapping(value = "/dUser/{id}")
    public void eliminarUserById(@PathVariable("id") int idUser) {
        uService.eliminarUsuario(idUser);
    }


}
