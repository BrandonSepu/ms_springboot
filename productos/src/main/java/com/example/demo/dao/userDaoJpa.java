package com.example.demo.dao;

import com.example.demo.models.userModel;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;
@Component
public interface userDaoJpa extends JpaRepository<userModel, Integer> {

    //userModel findByEmail(int id);
    //@Transactional
    //@Modifying
    //@Query("DELETE FROM USER as u WHERE u.id_user =?1")
    //void deleteById(int id);
}
