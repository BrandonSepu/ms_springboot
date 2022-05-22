package com.example.demo.dao.proDao;

import com.example.demo.models.productsModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

public interface productDaoJpa extends JpaRepository<productsModel, Integer> {

    @Modifying
    @Transactional
    @Query(value = "SELECT * FROM PRODUCTOS P INNER JOIN TIPO T ON P.tipo_id_tipo = T.ID_TIPO;", nativeQuery = true)
    List<productsModel> getTipoByProduct();
}
