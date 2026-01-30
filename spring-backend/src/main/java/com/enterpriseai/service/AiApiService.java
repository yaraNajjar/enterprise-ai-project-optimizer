package com.enterpriseai.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import java.util.HashMap;
import java.util.Map;

@Service
public class AiApiService {

    @Value("${AI_API_URL:http://localhost:8000}")
    private String BASE_URL;

    private final RestTemplate restTemplate = new RestTemplate();

    public Map<String, Object> predictFull(int teamSize, int issues) {
        String url = BASE_URL + "/predict_full";

        Map<String, Object> request = new HashMap<>();
        request.put("team_size", teamSize);
        request.put("issues", issues);

        // send POST request for FastAPI
        Map<String, Object> response = restTemplate.postForObject(url, request, Map.class);
        
        return response;
    }

    public Object getProjects() {
        String url = BASE_URL + "/projects";
        return restTemplate.getForObject(url, Object.class);
    }

}
