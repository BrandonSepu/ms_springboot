package com.example.demo.controllers;

import com.example.demo.models.ventasModel;
import com.example.demo.services.serviceVentas.ventasServiceImp;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins = "*")
@RestController
public class ventaController {

    @Autowired
    ventasServiceImp venService;

    @RequestMapping("/welcome")
    public String welcomepage() {
        return "Bienvenido a mi api";
    }

    @GetMapping(value = "/ventas", produces = MediaType.APPLICATION_JSON_VALUE)
    public List<ventasModel> getAllBodega() {
        return venService.getAllventas();
    }

    @GetMapping(value = "/venta/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
    public ventasModel getBodId(@PathVariable("id") int id) {
        return venService.getventas(id);
    }

    @PostMapping(value = "/loadInVenta", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.TEXT_PLAIN_VALUE)
    public String loadInBodega(@RequestBody ventasModel newVenta) {
        return String.valueOf(venService.createventas(newVenta));
    }

    @PutMapping(value = "/updateVenta", consumes = MediaType.APPLICATION_JSON_VALUE)
    public void updateBodega(@RequestBody ventasModel ventaCreated) {
        venService.updateventas(ventaCreated);
    }

    @DeleteMapping(value = "/delVenta/{id}")
    public void delBodPro(@PathVariable("id") int idVen) {
        venService.delventas(idVen);
    }
}
