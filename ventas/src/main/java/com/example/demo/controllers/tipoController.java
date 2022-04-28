package com.example.demo.controllers;

import com.example.demo.models.tipoPagoModel;
import com.example.demo.services.serviceTipo.tipoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins = "*")
@RestController
public class tipoController {

    @Autowired
    tipoService tService;

    @RequestMapping("/welcome3")
    public String welcomepage3() {
        return "Bienvenido a mi api";
    }

    @GetMapping(value = "/tipo", produces = MediaType.APPLICATION_JSON_VALUE)
    public List<tipoPagoModel> getAllTipo() {
        return tService.getAlltipo();
    }

    @GetMapping(value = "/tipo/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
    public tipoPagoModel getProId(@PathVariable("id") int id) {
        return tService.gettipo(id);
    }

    @PostMapping(value = "/loadTipo", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.TEXT_PLAIN_VALUE)
    public String loadTipo(@RequestBody tipoPagoModel newTipo) {
        return String.valueOf(tService.createtipo(newTipo));
    }

    @PutMapping(value = "/updateTipo", consumes = MediaType.APPLICATION_JSON_VALUE)
    public void updateTipo(@RequestBody tipoPagoModel tipoCreated) {
        tService.updatetipo(tipoCreated);
    }

    @DeleteMapping(value = "/delTipo/{id}")
    public void delTipo(@PathVariable("id") int idTipo) {
        tService.deltipo(idTipo);
    }

}
