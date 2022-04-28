package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.domain.EntityScan;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.data.jpa.repository.config.EnableJpaRepositories;


@SpringBootApplication
@ComponentScan(basePackages ={"com.example.demo.controllers","com.example.demo.dao","com.example.demo.dao.bodDao","com.example.demo.dao.proDao","com.example.demo.dao.tipDao","com.example.demo.services","com.example.demo.services.serviceBod.bodService","com.example.demo.services.servicePro","com.example.demo.services.serviceTipo"})
@EntityScan(basePackages ={"com.example.demo.models"})
@EnableJpaRepositories(basePackages ={"com.example.demo.dao"})
public class DemoApplication /*implements CommandLineRunner*/{

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}

	/*@Autowired
	userDao dao;
	@Override
	public void run(String... args) throws Exception {
		userModel user1 = new userModel("aaron2","20111321-8",16,"vendedor","aa1@gmail.com","aaro2n1");
		dao.agregarUser(user1);
	}*/
}
