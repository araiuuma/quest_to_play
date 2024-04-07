class AccountDAO:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def create_account(self, username, password, role):
        query = 'INSERT INTO accounts (username, password, role) VALUES (?, ?, ?)'
        params = (username, password, role)
        self.db_manager.execute_query(query, params)

    # 다른 메서드들도 동일하게 작성 가능

class MissionDAO:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def create_mission(self, title, description, reward_time, clear_condition):
        query = 'INSERT INTO missions (title, description, reward_time, clear_condition) VALUES (?, ?, ?, ?)'
        params = (title, description, reward_time, clear_condition)
        self.db_manager.execute_query(query, params)

    # 다른 메서드들도 동일하게 작성 가능

class TimeUsageDAO:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def record_time_usage(self, user_id, used_time, remaining_time):
        query = 'INSERT INTO time_usage (user_id, used_time, remaining_time) VALUES (?, ?, ?)'
        params = (user_id, used_time, remaining_time)
        self.db_manager.execute_query(query, params)

    # 다른 메서드들도 동일하게 작성 가능

# 사용 예시
if __name__ == "__main__":
    db_manager = DatabaseManager()
    db_manager.create_tables()

    account_dao = AccountDAO(db_manager)
    account_dao.create_account('parent1', 'password1', 'parent')

    mission_dao = MissionDAO(db_manager)
    mission_dao.create_mission('Mission 1', 'Description for Mission 1', 60, 'Clear condition for Mission 1')

    time_usage_dao = TimeUsageDAO(db_manager)
    time_usage_dao.record_time_usage(1, 30, 120)
