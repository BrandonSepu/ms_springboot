package com.example.demo.services.serviceTipo;

import com.example.demo.models.tipoModel;


import java.util.List;

public interface tipoService {
    boolean createtipo(tipoModel tipo);

    List<tipoModel> getAlltipo();

    boolean deltipo(int idTipo);

    tipoModel gettipo(int idTipo);

    void updatetipo(tipoModel tipo);
}
