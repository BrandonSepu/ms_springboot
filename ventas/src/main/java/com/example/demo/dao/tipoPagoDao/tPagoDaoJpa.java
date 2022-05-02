package com.example.demo.dao.tipoPagoDao;

import com.example.demo.models.tipoPagoModel;
import org.springframework.data.jpa.repository.JpaRepository;

public interface tPagoDaoJpa extends JpaRepository<tipoPagoModel, Integer> {

    //@Query("select * from tipo where id_tipo = ?")
    //void getById(int id);
}
