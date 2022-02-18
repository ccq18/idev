package dashboard.controller;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/test")
@Slf4j
public class DemoController {
    @Value("${timeout:0}")
    private String timeout;

    @GetMapping("hello")
    public String wasteForGood() {
        return "hello";
    }


    @GetMapping("timeout")
    public String gettimeout() {
        return timeout;
    }




}
