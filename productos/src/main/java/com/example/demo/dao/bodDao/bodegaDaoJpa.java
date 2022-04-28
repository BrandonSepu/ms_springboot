package com.example.demo.dao.bodDao;

import com.example.demo.models.bodegaModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface bodegaDaoJpa extends JpaRepository<bodegaModel, Integer> {

    //@Query("select * from bodega where id_bod = ?")
    //void getById(int id);
}
