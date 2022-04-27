package com.example.demo.dao.tipDao;

import com.example.demo.models.tipoModel;
import org.springframework.stereotype.Component;

import java.util.List;

@Component
public interface tipoDao {
    void createtipo(tipoModel tipo);

    List<tipoModel> getAlltipo();

    void deltipo(int idTipo);

    tipoModel gettipo(int idTipo);

    void updatetipo(tipoModel tipo);
}
