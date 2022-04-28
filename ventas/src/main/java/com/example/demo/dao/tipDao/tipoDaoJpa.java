package com.example.demo.dao.tipDao;

import com.example.demo.models.tipoPagoModel;
import org.springframework.data.jpa.repository.JpaRepository;

public interface tipoDaoJpa extends JpaRepository<tipoPagoModel, Integer> {

    //@Query("select * from tipo where id_tipo = ?")
    //void getById(int id);
}
