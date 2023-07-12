package solver;
import java.util.*;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import io.sentry.Sentry;
// import io.sentry.event.BreadcrumbBuilder;
// import io.sentry.event.UserBuilder;

/**
 * メイン処理を記載する
 */
public class Solver {
    public static void main(String[] args){
        Logger log = LogManager.getLogger(Solver.class);

        String sentry_dsn = System.getenv("SENTRY_DSN");
        log.info("sentry_dsn: {}", sentry_dsn);
        if (sentry_dsn == null) {
            log.error(" SENTRY_DSN should not be null");
            return;
        }
        Sentry.init(options -> {
            options.setDsn(sentry_dsn);
            options.setAttachStacktrace(false);
        });

        // ロギング
        // log.error("hello aaa" + 12345);
        log.error("hello {}", 12345);

        // 例外
        // String message = "5";
        // throw new Exception(message);
        // try {
        //     throw new Exception(message);
        // } catch (Exception e) {
        //     log.error("exception with message: " +  e.getMessage());
        // }

        // Solver.Hoge(log, message);

        // エラーメッセージ
        // log.error("hello {}", 12345);

        // long current_ms = System.currentTimeMillis();
        // log.error("current_ms {}", current_ms);
    }

    // public static void Hoge(Logger logger, String message) {
    //     logger.error(message);
    // }
}
