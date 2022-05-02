package com.example.demo.controllers;

import com.example.demo.models.detalleVenModel;
import com.example.demo.services.serviceDet.DetalleServiceImp;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins = "*")
@RestController
public class detVenController {

    @Autowired
    DetalleServiceImp venService;

    @RequestMapping("/welcome2")
    public String welcomepage2() {
        return "Bienvenido a mi api";
    }

    @GetMapping(value = "/DetallesVentas", produces = MediaType.APPLICATION_JSON_VALUE)
    public List<detalleVenModel> getAllDetalleVenta() {
        return venService.getAllDetalleVenta();
    }

    @GetMapping(value = "/DetalleVenta/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
    public detalleVenModel getDetVenId(@PathVariable("id") int id) {
        return venService.getDetalleVenta(id);
    }

    @PostMapping(value = "/loadDetalleVenta", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.TEXT_PLAIN_VALUE)
    public String loadDetalleVenta(@RequestBody detalleVenModel newDetVent) {
        return String.valueOf(venService.createDetalleVenta(newDetVent));
    }

    @PutMapping(value = "/updateDetalleVenta", consumes = MediaType.APPLICATION_JSON_VALUE)
    public void updateDetalleVenta(@RequestBody detalleVenModel detVenCreated) {
        venService.updateDetalleVenta(detVenCreated);
    }

    @DeleteMapping(value = "/delDetalleVenta/{id}")
    public void delDetVen(@PathVariable("id") int idDetVen) {
        venService.delDetalleVenta(idDetVen);
    }

}
