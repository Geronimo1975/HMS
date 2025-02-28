CREATE TABLE "accounts_profile"(
    "id" INTEGER NOT NULL,
    "next_report_date" TIMESTAMP(0) WITHOUT TIME ZONE NULL,
    "reports_allowed" SMALLINT NOT NULL,
    "user_id" INTEGER NULL,
    "ping_log_limit" INTEGER NOT NULL,
    "token" VARCHAR(255) NOT NULL,
    "check_limit" INTEGER NOT NULL,
    "last_sms_date" TIMESTAMP(0) WITHOUT TIME ZONE NULL,
    "sms_limit" INTEGER NOT NULL,
    "sms_sent" INTEGER NOT NULL,
    "team_limit" INTEGER NOT NULL,
    "sort" VARCHAR(255) NOT NULL,
    "nag_period" BIGINT NOT NULL,
    "next_nag_date" TIMESTAMP(0) WITHOUT TIME ZONE NULL,
    "deletion_notice_date" TIMESTAMP(0) WITHOUT TIME ZONE NULL,
    "last_active_date" TIMESTAMP(0) WITHOUT TIME ZONE NULL
);
ALTER TABLE
    "accounts_profile" ADD PRIMARY KEY("id");
ALTER TABLE
    "accounts_profile" ADD CONSTRAINT "accounts_profile_user_id_unique" UNIQUE("user_id");
CREATE TABLE "accounts_project"(
    "id" INTEGER NOT NULL,
    "code" CHAR(255) NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "api_key" VARCHAR(255) NOT NULL,
    "api_key_readonly" VARCHAR(255) NOT NULL,
    "owner_id" INTEGER NOT NULL,
    "badge_key" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "accounts_project" ADD PRIMARY KEY("id");
ALTER TABLE
    "accounts_project" ADD CONSTRAINT "accounts_project_code_unique" UNIQUE("code");
CREATE INDEX "accounts_project_api_key_index" ON
    "accounts_project"("api_key");
CREATE INDEX "accounts_project_api_key_readonly_index" ON
    "accounts_project"("api_key_readonly");
CREATE INDEX "accounts_project_owner_id_index" ON
    "accounts_project"("owner_id");
ALTER TABLE
    "accounts_project" ADD CONSTRAINT "accounts_project_badge_key_unique" UNIQUE("badge_key");
CREATE TABLE "accounts_member"(
    "id" INTEGER NOT NULL,
    "user_id" INTEGER NOT NULL,
    "project_id" INTEGER NOT NULL
);
ALTER TABLE
    "accounts_member" ADD PRIMARY KEY("id");
CREATE INDEX "accounts_member_user_id_index" ON
    "accounts_member"("user_id");
CREATE INDEX "accounts_member_project_id_index" ON
    "accounts_member"("project_id");
CREATE TABLE "api_channel"(
    "id" INTEGER NOT NULL,
    "code" CHAR(255) NOT NULL,
    "created" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "kind" VARCHAR(255) NOT NULL,
    "value" TEXT NOT NULL,
    "email_verified" SMALLINT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "project_id" INTEGER NOT NULL,
    "last_error" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "api_channel" ADD PRIMARY KEY("id");
ALTER TABLE
    "api_channel" ADD CONSTRAINT "api_channel_code_unique" UNIQUE("code");
CREATE INDEX "api_channel_project_id_index" ON
    "api_channel"("project_id");
CREATE TABLE "api_channel_checks"(
    "id" INTEGER NOT NULL,
    "channel_id" INTEGER NOT NULL,
    "check_id" INTEGER NOT NULL
);
ALTER TABLE
    "api_channel_checks" ADD CONSTRAINT "api_channel_checks_channel_id_check_id_unique" UNIQUE("channel_id", "check_id");
ALTER TABLE
    "api_channel_checks" ADD PRIMARY KEY("id");
CREATE INDEX "api_channel_checks_check_id_index" ON
    "api_channel_checks"("check_id");
CREATE TABLE "api_check"(
    "id" INTEGER NOT NULL,
    "code" CHAR(255) NOT NULL,
    "last_ping" TIMESTAMP(0) WITHOUT TIME ZONE NULL,
    "alert_after" TIMESTAMP(0) WITHOUT TIME ZONE NULL,
    "status" VARCHAR(255) NOT NULL,
    "timeout" BIGINT NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "created" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "grace" BIGINT NOT NULL,
    "tags" VARCHAR(255) NOT NULL,
    "n_pings" INTEGER NOT NULL,
    "kind" VARCHAR(255) NOT NULL,
    "schedule" VARCHAR(255) NOT NULL,
    "tz" VARCHAR(255) NOT NULL,
    "has_confirmation_link" SMALLINT NOT NULL,
    "last_ping_was_fail" SMALLINT NULL,
    "desc" TEXT NOT NULL,
    "last_start" TIMESTAMP(0) WITHOUT TIME ZONE NULL,
    "subject" VARCHAR(255) NOT NULL,
    "project_id" INTEGER NOT NULL,
    "last_duration" BIGINT NULL,
    "methods" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "api_check" ADD PRIMARY KEY("id");
ALTER TABLE
    "api_check" ADD CONSTRAINT "api_check_code_unique" UNIQUE("code");
CREATE INDEX "api_check_alert_after_index" ON
    "api_check"("alert_after");
CREATE INDEX "api_check_project_id_index" ON
    "api_check"("project_id");
CREATE TABLE "api_flip"(
    "id" INTEGER NOT NULL,
    "created" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "processed" TIMESTAMP(0) WITHOUT TIME ZONE NULL,
    "old_status" VARCHAR(255) NOT NULL,
    "new_status" VARCHAR(255) NOT NULL,
    "owner_id" INTEGER NOT NULL
);
ALTER TABLE
    "api_flip" ADD PRIMARY KEY("id");
CREATE INDEX "api_flip_processed_index" ON
    "api_flip"("processed");
CREATE INDEX "api_flip_owner_id_index" ON
    "api_flip"("owner_id");
CREATE TABLE "api_notification"(
    "id" INTEGER NOT NULL,
    "check_status" VARCHAR(255) NOT NULL,
    "created" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "channel_id" INTEGER NOT NULL,
    "owner_id" INTEGER NOT NULL,
    "error" VARCHAR(255) NOT NULL,
    "code" CHAR(255) NULL
);
ALTER TABLE
    "api_notification" ADD PRIMARY KEY("id");
CREATE INDEX "api_notification_channel_id_index" ON
    "api_notification"("channel_id");
CREATE INDEX "api_notification_owner_id_index" ON
    "api_notification"("owner_id");
CREATE TABLE "api_ping"(
    "id" BIGINT NOT NULL,
    "created" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "remote_addr" CHAR(255) NULL,
    "method" VARCHAR(255) NOT NULL,
    "ua" VARCHAR(255) NOT NULL,
    "owner_id" INTEGER NOT NULL,
    "scheme" VARCHAR(255) NOT NULL,
    "n" INTEGER NULL,
    "body" TEXT NULL,
    "kind" VARCHAR(255) NULL
);
ALTER TABLE
    "api_ping" ADD PRIMARY KEY("id");
CREATE INDEX "api_ping_owner_id_index" ON
    "api_ping"("owner_id");
CREATE TABLE "api_tokenbucket"(
    "id" INTEGER NOT NULL,
    "value" VARCHAR(255) NOT NULL,
    "tokens" DOUBLE PRECISION NOT NULL,
    "updated" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "api_tokenbucket" ADD PRIMARY KEY("id");
ALTER TABLE
    "api_tokenbucket" ADD CONSTRAINT "api_tokenbucket_value_unique" UNIQUE("value");
CREATE TABLE "auth_user"(
    "id" INTEGER NOT NULL,
    "password" VARCHAR(255) NOT NULL,
    "last_login" TIMESTAMP(0) WITHOUT TIME ZONE NULL,
    "is_superuser" SMALLINT NOT NULL,
    "username" VARCHAR(255) NOT NULL,
    "first_name" VARCHAR(255) NOT NULL,
    "last_name" VARCHAR(255) NOT NULL,
    "email" VARCHAR(255) NOT NULL,
    "is_staff" SMALLINT NOT NULL,
    "is_active" SMALLINT NOT NULL,
    "date_joined" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "auth_user" ADD PRIMARY KEY("id");
ALTER TABLE
    "auth_user" ADD CONSTRAINT "auth_user_username_unique" UNIQUE("username");
CREATE TABLE "payments_subscription"(
    "id" INTEGER NOT NULL,
    "customer_id" VARCHAR(255) NOT NULL,
    "payment_method_token" VARCHAR(255) NOT NULL,
    "subscription_id" VARCHAR(255) NOT NULL,
    "user_id" INTEGER NULL,
    "plan_id" VARCHAR(255) NOT NULL,
    "address_id" VARCHAR(255) NOT NULL,
    "send_invoices" SMALLINT NOT NULL,
    "plan_name" VARCHAR(255) NOT NULL,
    "invoice_email" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "payments_subscription" ADD PRIMARY KEY("id");
ALTER TABLE
    "payments_subscription" ADD CONSTRAINT "payments_subscription_user_id_unique" UNIQUE("user_id");
ALTER TABLE
    "api_notification" ADD CONSTRAINT "api_notification_owner_id_foreign" FOREIGN KEY("owner_id") REFERENCES "api_check"("id");
ALTER TABLE
    "api_notification" ADD CONSTRAINT "api_notification_channel_id_foreign" FOREIGN KEY("channel_id") REFERENCES "api_channel"("id");
ALTER TABLE
    "accounts_project" ADD CONSTRAINT "accounts_project_owner_id_foreign" FOREIGN KEY("owner_id") REFERENCES "auth_user"("id");
ALTER TABLE
    "accounts_member" ADD CONSTRAINT "accounts_member_project_id_foreign" FOREIGN KEY("project_id") REFERENCES "accounts_project"("id");
ALTER TABLE
    "accounts_profile" ADD CONSTRAINT "accounts_profile_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "auth_user"("id");
ALTER TABLE
    "api_channel" ADD CONSTRAINT "api_channel_project_id_foreign" FOREIGN KEY("project_id") REFERENCES "accounts_project"("id");
ALTER TABLE
    "api_check" ADD CONSTRAINT "api_check_project_id_foreign" FOREIGN KEY("project_id") REFERENCES "accounts_project"("id");
ALTER TABLE
    "api_channel_checks" ADD CONSTRAINT "api_channel_checks_check_id_foreign" FOREIGN KEY("check_id") REFERENCES "api_check"("id");
ALTER TABLE
    "api_flip" ADD CONSTRAINT "api_flip_owner_id_foreign" FOREIGN KEY("owner_id") REFERENCES "api_check"("id");
ALTER TABLE
    "payments_subscription" ADD CONSTRAINT "payments_subscription_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "auth_user"("id");
ALTER TABLE
    "api_channel_checks" ADD CONSTRAINT "api_channel_checks_channel_id_foreign" FOREIGN KEY("channel_id") REFERENCES "api_channel"("id");
ALTER TABLE
    "api_ping" ADD CONSTRAINT "api_ping_owner_id_foreign" FOREIGN KEY("owner_id") REFERENCES "api_check"("id");
ALTER TABLE
    "accounts_member" ADD CONSTRAINT "accounts_member_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "auth_user"("id");