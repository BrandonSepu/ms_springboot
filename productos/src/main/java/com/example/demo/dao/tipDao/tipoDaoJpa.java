package com.example.demo.dao.tipDao;

import com.example.demo.models.tipoModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface tipoDaoJpa extends JpaRepository<tipoModel, Integer> {

    //@Query("select * from tipo where id_tipo = ?")
    //void getById(int id);
}
