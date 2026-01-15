package com.enterpriseai.controller;

import com.enterpriseai.service.AiApiService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.CrossOrigin;

import java.util.Map;

@RestController
@CrossOrigin(origins = "http://localhost:5173")
public class AiController {

    private final AiApiService aiApiService;

    public AiController(AiApiService aiApiService) {
        this.aiApiService = aiApiService;
    }

    @GetMapping("/predict/{teamSize}/{issues}")
    public Map<String, Object> predict(@PathVariable int teamSize, @PathVariable int issues) {
        return aiApiService.predictFull(teamSize, issues);
    }

    @GetMapping("/projects")
    public Object getProjects() {
        return aiApiService.getProjects();
    }
}
