package com.example.demo.controllers;

import com.example.demo.models.ventasModel;
import com.example.demo.services.serviceBod.bodService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins = "*")
@RestController
public class bodegaController {

    @Autowired
    bodService bService;

    @RequestMapping("/welcome")
    public String welcomepage() {
        return "Bienvenido a mi api";
    }

    @GetMapping(value = "/bodega", produces = MediaType.APPLICATION_JSON_VALUE)
    public List<ventasModel> getAllBodega() {
        return bService.getAllBodegaPro();
    }

    @GetMapping(value = "/bodega/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
    public ventasModel getBodId(@PathVariable("id") int id) {
        return bService.getBodegaPro(id);
    }

    @PostMapping(value = "/loadInBodega", consumes = MediaType.APPLICATION_JSON_VALUE, produces = MediaType.TEXT_PLAIN_VALUE)
    public String loadInBodega(@RequestBody ventasModel newBodPro) {
        return String.valueOf(bService.createBodegaPro(newBodPro));
    }

    @PutMapping(value = "/updateBodega", consumes = MediaType.APPLICATION_JSON_VALUE)
    public void updateBodega(@RequestBody ventasModel bodCreated) {
        bService.updateBodegaPro(bodCreated);
    }

    @DeleteMapping(value = "/delBodPro/{id}")
    public void delBodPro(@PathVariable("id") int idbod) {
        bService.delBodegaPro(idbod);
    }
}
