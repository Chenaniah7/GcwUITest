package starter.wikipedia;

import net.serenitybdd.junit5.SerenityJUnit5Extension;
import net.serenitybdd.screenplay.Actor;
import net.serenitybdd.screenplay.ensure.Ensure;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import net.serenitybdd.screenplay.annotations.CastMember;

@ExtendWith(SerenityJUnit5Extension.class)
public class SerenitySampleTest {

    @CastMember(name = "wendy")  //定义一个actor，同时这个注解会自动管理webDriver,不需要再手动下载wedDriver到本地
    Actor wendy;

    @Test
    void searchBySingleKeyword() {
        wendy.attemptsTo(
                Navigate.toTheHomePage()

        );
    }
}
